import { useState, useEffect } from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { useFetchMeta } from '../../hooks/useFetchMeta';
import { useToggleSet } from '../../hooks/useToggleSet';
import { useAllDenborak } from '../../hooks/useAllDenborak';
import AditzakToggle from '../../components/AditzakToggle';
import AriketaFooter from '../../components/AriketaFooter';
import { cap } from '../../utils/format';

type AditzakStructure = { [modua: string]: { [denbora: string]: string | undefined } };
type RandomResponse = {
    success: boolean;
    infinitiboa: string;
    nor: string; nori: string; nork: string;
    aditzak: AditzakStructure;
};

type FetchKey = { aditza: string; n: number };

const Home = () => {
    const { data: metaData } = useFetchMeta();
    const meta = metaData?.data;

    const [selectedAditzak, setSelectedAditzak, toggleAditza] = useToggleSet();
    const [fetchKey, setFetchKey] = useState<FetchKey | null>(null);
    const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
    const [showSolutions, setShowSolutions] = useState(false);
    const [results, setResults] = useState<Record<string, boolean | null>>({});

    useEffect(() => {
        if (meta) setSelectedAditzak(new Set(meta.aditzak.map(a => a.value)));
    }, [meta]);

    useEffect(() => {
        if (meta && !fetchKey) {
            const aditzak = meta.aditzak.map(a => a.value);
            const aditza = aditzak[Math.floor(Math.random() * aditzak.length)];
            setFetchKey({ aditza, n: 0 });
        }
    }, [meta, fetchKey]);

    const { data, isFetching, error } = useQuery({
        queryKey: ['table-random', fetchKey],
        queryFn: () => axios.get<RandomResponse>(`${process.env.REACT_APP_API_URL}/table/random`, {
            params: { aditza: fetchKey!.aditza }
        }),
        enabled: !!fetchKey,
        staleTime: Infinity,
        refetchOnWindowFocus: false,
    });

    const aditzData = data?.data;

    const allDenborak = useAllDenborak(meta);

    useEffect(() => {
        setUserAnswers({});
        setShowSolutions(false);
        setResults({});
    }, [aditzData]);

    const birsortu = () => {
        const aditzak = Array.from(selectedAditzak);
        const aditza = aditzak[Math.floor(Math.random() * aditzak.length)];
        setFetchKey(prev => ({ aditza, n: (prev?.n ?? 0) + 1 }));
    };

    const checkAnswers = () => {
        if (!meta || !aditzData) return;
        const newResults: Record<string, boolean | null> = {};
        for (const m of meta.moduak) {
            for (const d of m.denborak) {
                const correct = aditzData.aditzak[m.value]?.[d.value];
                if (correct) {
                    const key = `${m.value}-${d.value}`;
                    newResults[key] = userAnswers[key]?.trim().toLowerCase() === correct.toLowerCase();
                }
            }
        }
        setResults(newResults);
    };

    if (!meta || (!aditzData && !error)) return (
        <div className="p-8 text-center font-serif italic">Kargatzen...</div>
    );
    if (error && !aditzData) return (
        <div className="p-8 text-center text-red-600 font-serif italic">Errorea: ezin da zerbitzarira konektatu.</div>
    );

    return (
        <div className="max-w-5xl mx-auto p-8 font-sans text-slate-800">
            <header className="mb-8 text-center">
                <h1 className="text-3xl font-light tracking-widest uppercase mb-4 text-slate-600">Aditz Ariketa</h1>

                <AditzakToggle aditzak={meta.aditzak} selected={selectedAditzak} onToggle={toggleAditza} />

                <div className="flex justify-center gap-8 bg-slate-50 p-6 rounded-xl shadow-sm border border-slate-100">
                    <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">Infinitiboa</span><span className="text-xl font-semibold text-indigo-700">{cap(aditzData?.infinitiboa ?? '')}</span></div>
                    <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NOR</span><span className="text-xl font-medium">{aditzData?.nor}</span></div>
                    <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NORI</span><span className="text-xl font-medium">{aditzData?.nori !== 'NONE' ? aditzData?.nori : '—'}</span></div>
                    <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NORK</span><span className="text-xl font-medium">{aditzData?.nork !== 'NONE' ? aditzData?.nork : '—'}</span></div>
                </div>
            </header>

            <div className="overflow-hidden rounded-lg border border-slate-200 shadow-lg">
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
                        {meta.moduak.map(m => (
                            <tr key={m.value} className="hover:bg-slate-50 transition-colors">
                                <td className="px-6 py-4 font-semibold capitalize text-slate-600 bg-slate-50/50">{m.label}</td>
                                {allDenborak.map(d => {
                                    const solution = aditzData?.aditzak[m.value]?.[d.value];
                                    const key = `${m.value}-${d.value}`;
                                    return (
                                        <td key={d.value} className="px-6 py-4">
                                            {!solution ? (
                                                <div className="h-10 bg-slate-100 rounded-md opacity-40 cursor-not-allowed" />
                                            ) : (
                                                <div className="space-y-2">
                                                    <input
                                                        type="text"
                                                        value={userAnswers[key] || ''}
                                                        onChange={e => setUserAnswers(prev => ({ ...prev, [key]: e.target.value }))}
                                                        disabled={showSolutions}
                                                        className={`w-full px-3 py-2 rounded border outline-none transition-all ${
                                                            results[key] === true  ? 'border-green-500 bg-green-50' :
                                                            results[key] === false ? 'border-red-500 bg-red-50' :
                                                            'border-slate-300 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'
                                                        }`}
                                                    />
                                                    {showSolutions && (
                                                        <p className="text-xs font-bold text-indigo-600 animate-bounce">{solution}</p>
                                                    )}
                                                </div>
                                            )}
                                        </td>
                                    );
                                })}
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

export default Home;
