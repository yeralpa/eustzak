import { useState, useMemo } from 'react';
import { useFetchFull, FullParams } from '../../hooks/useFetchFull';
import { useFetchMeta } from '../../hooks/useFetchMeta';
import { cap } from '../../utils/format';

const selectClass = "px-3 py-2 rounded border border-slate-300 bg-white text-slate-800 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 text-sm cursor-pointer";

const Bilaketa = () => {
    const { data: metaData } = useFetchMeta();
    const meta = metaData?.data;

    const [aditza, setAditza] = useState('IZAN');
    const [nor,  setNor]  = useState('NI');
    const [nori, setNori] = useState('NONE');
    const [nork, setNork] = useState('NONE');
    const [params, setParams] = useState<FullParams | null>(null);

    const { data, isFetching, error } = useFetchFull(params);
    const aditzData = data?.data;

    const allDenborak = useMemo(() => {
        if (!meta) return [];
        const seen = new Set<string>();
        const result: { value: string; label: string }[] = [];
        for (const m of meta.moduak) {
            for (const d of m.denborak) {
                if (!seen.has(d.value)) { seen.add(d.value); result.push(d); }
            }
        }
        return result;
    }, [meta]);

    const pertsonak = meta?.pertsonak ?? [];

    return (
        <div className="max-w-5xl mx-auto p-8 font-sans text-slate-800">
            <header className="mb-8 text-center">
                <h1 className="text-3xl font-light tracking-widest uppercase mb-4 text-slate-600">Aditz Bilaketa</h1>
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
                        <span className="text-xs uppercase tracking-tighter text-slate-400">NOR</span>
                        <select value={nor} onChange={e => setNor(e.target.value)} className={selectClass}>
                            {pertsonak.map(p => (
                                <option key={p.value} value={p.value}>{p.nor}</option>
                            ))}
                        </select>
                    </div>
                    <div className="flex flex-col gap-1">
                        <span className="text-xs uppercase tracking-tighter text-slate-400">NORI</span>
                        <select value={nori} onChange={e => setNori(e.target.value)} className={selectClass}>
                            <option value="NONE">—</option>
                            {pertsonak.map(p => (
                                <option key={p.value} value={p.value}>{p.nori}</option>
                            ))}
                        </select>
                    </div>
                    <div className="flex flex-col gap-1">
                        <span className="text-xs uppercase tracking-tighter text-slate-400">NORK</span>
                        <select value={nork} onChange={e => setNork(e.target.value)} className={selectClass}>
                            <option value="NONE">—</option>
                            {pertsonak.map(p => (
                                <option key={p.value} value={p.value}>{p.nork}</option>
                            ))}
                        </select>
                    </div>
                    <button
                        onClick={() => setParams({ aditza, nor, nori, nork })}
                        disabled={isFetching || !meta}
                        className="px-6 py-2 bg-indigo-600 text-white rounded-full font-medium hover:bg-indigo-700 shadow-md hover:shadow-indigo-200 transition-all disabled:opacity-50"
                    >
                        {isFetching ? 'Bilatzen...' : 'Bilatu'}
                    </button>
                </div>
                {error && (
                    <p className="mt-4 text-red-600 font-serif italic text-sm">
                        Errorea: konbinaketa baliogabea edo zerbitzarira ezin izan da konektatu.
                    </p>
                )}
            </header>

            {aditzData && (
                <>
                    <div className="mb-6 flex justify-center gap-8 bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">Infinitiboa</span><span className="text-xl font-semibold text-indigo-700">{cap(aditzData.infinitiboa)}</span></div>
                        <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NOR</span><span className="text-xl font-medium">{aditzData.nor}</span></div>
                        <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NORI</span><span className="text-xl font-medium">{aditzData.nori !== 'NONE' ? aditzData.nori : '—'}</span></div>
                        <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NORK</span><span className="text-xl font-medium">{aditzData.nork !== 'NONE' ? aditzData.nork : '—'}</span></div>
                    </div>

                    <div className="overflow-x-auto rounded-lg border border-slate-200 shadow-lg">
                        <table className="w-full border-collapse bg-white text-left text-sm">
                            <thead className="bg-slate-800 text-slate-50">
                                <tr>
                                    <th className="px-6 py-4 font-medium uppercase tracking-wider">Modua / Denbora</th>
                                    {allDenborak.map(d => (
                                        <th key={d.value} className="px-6 py-4 font-medium uppercase tracking-wider">{d.label}</th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-100">
                                {(meta?.moduak ?? []).map(m => (
                                    <tr key={m.value} className="hover:bg-slate-50 transition-colors">
                                        <td className="px-6 py-4 font-semibold capitalize text-slate-600 bg-slate-50/50">{m.label}</td>
                                        {allDenborak.map(d => {
                                            const value = aditzData.aditzak[m.value]?.[d.value];
                                            return (
                                                <td key={d.value} className="px-6 py-4">
                                                    {value
                                                        ? <span className="font-medium text-slate-800">{value}</span>
                                                        : <div className="h-6 bg-slate-100 rounded-md opacity-40" />
                                                    }
                                                </td>
                                            );
                                        })}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </>
            )}
        </div>
    );
};

export default Bilaketa;
