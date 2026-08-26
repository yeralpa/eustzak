import { useState, useEffect } from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { useFetchMeta } from '../../hooks/useFetchMeta';
import { RandomItem } from '../../hooks/useFetchMultiRandom';
import { useToggleSet } from '../../hooks/useToggleSet';
import AditzakToggle from '../../components/AditzakToggle';
import AriketaFooter from '../../components/AriketaFooter';
import { cap, person } from '../../utils/format';

const ROW_OPTIONS = [1, 5, 10, 20];

type MultiRandom = { success: boolean; items: RandomItem[] };

const Errenkadak = () => {
    const { data: metaData } = useFetchMeta();
    const meta = metaData?.data;

    const [selectedAditzak, setSelectedAditzak, toggleAditza] = useToggleSet();
    const [rowCount, setRowCount] = useState(5);
    const [aditzakParam, setAditzakParam] = useState<string | null>(null);
    const [counter, setCounter] = useState(0);

    const [userAnswers, setUserAnswers] = useState<Record<number, string>>({});
    const [showSolutions, setShowSolutions] = useState(false);
    const [results, setResults] = useState<Record<number, boolean | null>>({});

    useEffect(() => {
        if (meta) {
            const all = meta.aditzak.map(a => a.value);
            setSelectedAditzak(new Set(all));
            setAditzakParam(all.join(','));
        }
    }, [meta]);

    const { data, isFetching, error } = useQuery({
        queryKey: ['multi-random', rowCount, aditzakParam, counter],
        queryFn: () => axios.get<MultiRandom>(`${process.env.REACT_APP_API_URL}/conjugations/random`, {
            params: { n: rowCount, aditzak: aditzakParam }
        }),
        enabled: !!aditzakParam,
        staleTime: Infinity,
        refetchOnWindowFocus: false,
    });

    const items = data?.data.items ?? [];

    useEffect(() => {
        setUserAnswers({});
        setShowSolutions(false);
        setResults({});
    }, [data]);

    const birsortu = () => {
        const aditzak = Array.from(selectedAditzak).join(',');
        setAditzakParam(aditzak);
        setCounter(c => c + 1);
    };

    const checkAnswers = () => {
        const newResults: Record<number, boolean | null> = {};
        items.forEach((item, idx) => {
            newResults[idx] = userAnswers[idx]?.trim().toLowerCase() === item.aditza.toLowerCase();
        });
        setResults(newResults);
    };

    if (!meta || (!data && !error)) return (
        <div className="p-8 text-center font-serif italic">Kargatzen...</div>
    );
    if (error && !data) return (
        <div className="p-8 text-center text-red-600 font-serif italic">Errorea: ezin da zerbitzarira konektatu.</div>
    );

    return (
        <div className="max-w-5xl mx-auto p-8 font-sans text-slate-800">
            <header className="mb-8 text-center">
                <h1 className="text-3xl font-light tracking-widest uppercase mb-4 text-slate-600">Aditz Ariketa II</h1>

                <AditzakToggle aditzak={meta.aditzak} selected={selectedAditzak} onToggle={toggleAditza} />

                <div className="flex justify-center items-center gap-4 bg-slate-50 p-6 rounded-xl shadow-sm border border-slate-100">
                    <span className="text-xs uppercase tracking-tighter text-slate-400">Errenkada kopurua</span>
                    <div className="flex gap-2">
                        {ROW_OPTIONS.map(n => (
                            <button
                                key={n}
                                onClick={() => setRowCount(n)}
                                className={`px-4 py-1 rounded-full text-sm font-medium transition-all ${
                                    rowCount === n
                                        ? 'bg-indigo-600 text-white'
                                        : 'bg-slate-200 text-slate-600 hover:bg-slate-300'
                                }`}
                            >
                                {n}
                            </button>
                        ))}
                    </div>
                </div>
            </header>

            <div className="overflow-x-auto rounded-lg border border-slate-200 shadow-lg">
                <table className="min-w-full border-collapse bg-white text-left text-sm">
                    <thead className="bg-slate-800 text-slate-50">
                        <tr>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">Aditza</th>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">Modua</th>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">Denbora</th>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">NOR</th>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">NORI</th>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">NORK</th>
                            <th className="px-4 py-4 font-medium uppercase tracking-wider">Forma</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                        {items.map((item, idx) => (
                            <tr key={idx} className="hover:bg-slate-50 transition-colors">
                                <td className="px-4 py-4 font-semibold text-indigo-700">{cap(item.infinitiboa)}</td>
                                <td className="px-4 py-4 text-slate-600">{cap(item.modua)}</td>
                                <td className="px-4 py-4 text-slate-600">{cap(item.denbora)}</td>
                                <td className="px-4 py-4 text-slate-600">{person(item.nor)}</td>
                                <td className="px-4 py-4 text-slate-400">{person(item.nori)}</td>
                                <td className="px-4 py-4 text-slate-400">{person(item.nork)}</td>
                                <td className="px-4 py-4">
                                    <div className="space-y-1">
                                        <div className="grid min-w-[10ch]">
                                            <input
                                                type="text"
                                                value={userAnswers[idx] || ''}
                                                onChange={e => setUserAnswers(prev => ({ ...prev, [idx]: e.target.value }))}
                                                disabled={showSolutions}
                                                className={`col-start-1 row-start-1 w-full px-3 py-2 rounded border outline-none transition-all ${
                                                    results[idx] === true  ? 'border-green-500 bg-green-50' :
                                                    results[idx] === false ? 'border-red-500 bg-red-50' :
                                                    'border-slate-300 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'
                                                }`}
                                            />
                                            <span className="col-start-1 row-start-1 invisible px-3 py-2 whitespace-pre" aria-hidden="true">
                                                {userAnswers[idx] || ''}
                                            </span>
                                        </div>
                                        {showSolutions && (
                                            <p className="text-xs font-bold text-indigo-600 animate-bounce">{item.aditza}</p>
                                        )}
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <AriketaFooter
                onBirsortu={birsortu}
                onZuzendu={checkAnswers}
                onToggleSolutions={() => setShowSolutions(s => !s)}
                isFetching={isFetching}
                showSolutions={showSolutions}
            />
        </div>
    );
};

export default Errenkadak;
