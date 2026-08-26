import { useState, useEffect, useMemo } from 'react';
import { useFetchFullTable, Mota, FullTableParams } from '../../hooks/useFetchFullTable';
import { useFetchMeta } from '../../hooks/useFetchMeta';
import { useToggleSet } from '../../hooks/useToggleSet';

const NOR_NNK = ['hura', 'haiek'];
const NOR_NNK_LABEL: Record<string, string> = {
    hura: 'Singularra (hura)', haiek: 'Plurala (haiek)',
};

const selectClass = "px-3 py-2 rounded border border-slate-300 bg-white text-slate-800 outline-none focus:border-violet-500 focus:ring-1 focus:ring-violet-500 text-sm cursor-pointer";

type Col = { key: string; label: string };

const Table2D = ({ rowHeader, cols, rows, getValue }: {
    rowHeader: string;
    cols: Col[];
    rows: string[];
    getValue: (row: string, colKey: string) => string | null | undefined;
}) => (
    <div className="overflow-x-auto rounded-lg border border-slate-200 shadow-sm">
        <table className="border-collapse text-sm w-full bg-white">
            <thead className="bg-slate-800 text-slate-50">
                <tr>
                    <th className="px-4 py-3 text-left font-medium whitespace-nowrap uppercase tracking-wider">
                        {rowHeader}
                    </th>
                    {cols.map(col => (
                        <th key={col.key} className="px-4 py-3 text-left font-medium whitespace-nowrap uppercase tracking-wider">
                            {col.label}
                        </th>
                    ))}
                </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
                {rows.map(row => (
                    <tr key={row} className="hover:bg-slate-50 transition-colors">
                        <td className="px-4 py-3 font-semibold text-slate-600 bg-slate-50/50 whitespace-nowrap">
                            {row}
                        </td>
                        {cols.map(col => {
                            const val = getValue(row, col.key);
                            return (
                                <td key={col.key} className="px-4 py-3">
                                    {val
                                        ? <span className="font-medium text-slate-800">{val}</span>
                                        : <div className="h-4 w-12 rounded bg-slate-100 opacity-50" />
                                    }
                                </td>
                            );
                        })}
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
);

const Bilaketa2 = () => {
    const { data: metaData } = useFetchMeta();
    const meta = metaData?.data;

    const [aditza, setAditza] = useState('IZAN');
    const [mota, setMota]     = useState<Mota>('nor');
    const [selectedModuak, setSelectedModuak, toggleModua] = useToggleSet();
    const [params, setParams] = useState<FullTableParams | null>(null);

    useEffect(() => {
        if (meta) setSelectedModuak(new Set(meta.moduak.map(m => m.value)));
    }, [meta]);

    const currentMotak = useMemo(
        () => meta?.aditzak.find(a => a.value === aditza)?.motak ?? [],
        [meta, aditza]
    );

    const norForms  = meta?.pertsonak.map(p => p.nor)  ?? [];
    const noriForms = meta?.pertsonak.map(p => p.nori) ?? [];
    const norkForms = meta?.pertsonak.map(p => p.nork) ?? [];

    useEffect(() => {
        if (currentMotak.length > 0 && !currentMotak.includes(mota)) {
            setMota(currentMotak[0] as Mota);
        }
    }, [aditza, currentMotak]);

    const { data: axiosData, isFetching, error } = useFetchFullTable(params);
    const result = axiosData?.data;

    const renderContent = () => {
        if (!result || !meta) return null;
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const data = result.data as Record<string, any>;

        return meta.moduak
            .filter(m => selectedModuak.has(m.value))
            .map(modua => {
                const moduaData = data[modua.value];
                if (!moduaData) return null;
                const denborak = modua.denborak.filter(d => moduaData[d.value]);

                return (
                    <section key={modua.value} className="mb-10">
                        <h2 className="text-xl font-bold text-slate-700 mb-4 pb-2 border-b border-slate-200">
                            {modua.label}
                        </h2>

                        {result.mota === 'nor' && (
                            <Table2D
                                rowHeader="NOR"
                                cols={denborak.map(d => ({ key: d.value, label: d.label }))}
                                rows={norForms}
                                getValue={(nor, denbora) => moduaData[denbora]?.[nor]}
                            />
                        )}

                        {(result.mota === 'nor-nori' || result.mota === 'nor-nork') && (
                            <div className="flex flex-col gap-6">
                                {denborak.map(d => (
                                    <div key={d.value}>
                                        <h3 className="text-xs font-bold uppercase tracking-widest text-slate-400 mb-2">
                                            {d.label}
                                        </h3>
                                        <Table2D
                                            rowHeader={result.mota === 'nor-nori' ? 'NOR \\ NORI' : 'NOR \\ NORK'}
                                            cols={
                                                result.mota === 'nor-nori'
                                                    ? noriForms.map(f => ({ key: f, label: f }))
                                                    : norkForms.map(f => ({ key: f, label: f }))
                                            }
                                            rows={norForms}
                                            getValue={(nor, col) => moduaData[d.value]?.[nor]?.[col]}
                                        />
                                    </div>
                                ))}
                            </div>
                        )}

                        {result.mota === 'nor-nori-nork' && (
                            <div className="flex flex-col gap-8">
                                {denborak.map(d => (
                                    <div key={d.value}>
                                        <h3 className="text-xs font-bold uppercase tracking-widest text-slate-400 mb-4">
                                            {d.label}
                                        </h3>
                                        <div className="flex flex-col gap-4">
                                            {NOR_NNK.map(nor => (
                                                <div key={nor}>
                                                    <h4 className="text-xs font-bold uppercase tracking-widest text-violet-600 mb-2">
                                                        {NOR_NNK_LABEL[nor]}
                                                    </h4>
                                                    <Table2D
                                                        rowHeader="NORK \\ NORI"
                                                        cols={noriForms.map(f => ({ key: f, label: f }))}
                                                        rows={norkForms}
                                                        getValue={(nork, nori) => moduaData[d.value]?.[nor]?.[nork]?.[nori]}
                                                    />
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </section>
                );
            });
    };

    return (
        <div className="max-w-5xl mx-auto p-8 font-sans text-slate-800">
            <header className="mb-8 text-center">
                <h1 className="text-3xl font-light tracking-widest uppercase mb-4 text-slate-600">
                    Aditz Bilaketa II
                </h1>
                <div className="flex flex-wrap justify-center items-end gap-6 bg-slate-50 p-6 rounded-xl shadow-sm border border-slate-100">
                    <div className="flex flex-col gap-1">
                        <span className="text-xs uppercase tracking-tighter text-slate-400">Aditza</span>
                        <select value={aditza} onChange={e => setAditza(e.target.value)} className={selectClass}>
                            {(meta?.aditzak ?? []).map(a => (
                                <option key={a.value} value={a.value}>{a.label}</option>
                            ))}
                        </select>
                    </div>
                    <div className="flex flex-col gap-1">
                        <span className="text-xs uppercase tracking-tighter text-slate-400">Mota</span>
                        <select value={mota} onChange={e => setMota(e.target.value as Mota)} className={selectClass}>
                            {currentMotak.map(m => (
                                <option key={m} value={m}>{m.toUpperCase()}</option>
                            ))}
                        </select>
                    </div>
                    <div className="flex flex-col gap-1">
                        <span className="text-xs uppercase tracking-tighter text-slate-400">Moduak</span>
                        <div className="flex gap-1">
                            {(meta?.moduak ?? []).map(m => (
                                <button
                                    key={m.value}
                                    type="button"
                                    onClick={() => toggleModua(m.value)}
                                    className={`px-3 py-2 rounded text-sm font-medium border transition-colors ${
                                        selectedModuak.has(m.value)
                                            ? 'bg-violet-600 text-white border-violet-600'
                                            : 'bg-white text-slate-500 border-slate-300 hover:border-violet-400'
                                    }`}
                                >
                                    {m.label}
                                </button>
                            ))}
                        </div>
                    </div>
                    <button
                        onClick={() => setParams({ aditza, mota })}
                        disabled={isFetching || !meta}
                        className="px-6 py-2 bg-violet-600 text-white rounded-full font-medium hover:bg-violet-700 shadow-md hover:shadow-violet-200 transition-all disabled:opacity-50"
                    >
                        {isFetching ? 'Bilatzen...' : 'Bilatu'}
                    </button>
                </div>
                {error && (
                    <p className="mt-4 text-red-600 font-serif italic text-sm">
                        Errorea: zerbitzarira ezin izan da konektatu.
                    </p>
                )}
            </header>

            {renderContent()}
        </div>
    );
};

export default Bilaketa2;
