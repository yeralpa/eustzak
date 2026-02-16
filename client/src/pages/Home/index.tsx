import React, { useState, useEffect } from 'react';
import { useFetchRandom } from '../../hooks/useFetchRandom';

const MODUAK = ['indikatiboa', 'baldintza', 'ahalera', 'subjuntiboa'];
const DENBORAK = ['orain', 'lehen', 'alegiazkoa'];

const Home = () => {
  const { data, isLoading, refetch, isFetching } = useFetchRandom();
  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [showSolutions, setShowSolutions] = useState(false);
  const [results, setResults] = useState<Record<string, boolean | null>>({});

  const aditzData = data?.data;

  useEffect(() => {
    setUserAnswers({});
    setShowSolutions(false);
    setResults({});
  }, [aditzData]);

  const handleInputChange = (modua: string, denbora: string, value: string) => {
    setUserAnswers(prev => ({ ...prev, [`${modua}-${denbora}`]: value }));
  };

  const checkAnswers = () => {
    const newResults: Record<string, boolean | null> = {};
    MODUAK.forEach(m => {
      DENBORAK.forEach(d => {
        const correct = aditzData?.aditzak[m]?.[d];
        if (correct) {
          const userVal = userAnswers[`${m}-${d}`]?.trim().toLowerCase();
          newResults[`${m}-${d}`] = userVal === correct.toLowerCase();
        }
      });
    });
    setResults(newResults);
  };

  if (isLoading) return <div className="p-8 text-center font-serif italic">Kargatzen...</div>;

  return (
    <div className="max-w-5xl mx-auto p-8 font-sans text-slate-800">
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-light tracking-widest uppercase mb-4 text-slate-600">Aditz Ariketa</h1>
        <div className="flex justify-center gap-8 bg-slate-50 p-6 rounded-xl shadow-sm border border-slate-100">
          <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">Infinitiboa</span><span className="text-xl font-semibold text-indigo-700">{aditzData?.infinitiboa}</span></div>
          <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NOR</span><span className="text-xl font-medium">{aditzData?.nor}</span></div>
          <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NORI</span><span className="text-xl font-medium">{aditzData?.nori || "—"}</span></div>
          <div className="flex flex-col"><span className="text-xs uppercase tracking-tighter text-slate-400">NORK</span><span className="text-xl font-medium">{aditzData?.nork || "—"}</span></div>
        </div>
      </header>

      <div className="overflow-hidden rounded-lg border border-slate-200 shadow-lg">
        <table className="w-full border-collapse bg-white text-left text-sm">
          <thead className="bg-slate-800 text-slate-50">
            <tr>
              <th className="px-6 py-4 font-medium uppercase tracking-wider">Modua / Denbora</th>
              <th className="px-6 py-4 font-medium uppercase tracking-wider">Orainaldia</th>
              <th className="px-6 py-4 font-medium uppercase tracking-wider">Lehenaldia</th>
              <th className="px-6 py-4 font-medium uppercase tracking-wider">Alegiazkoa</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {MODUAK.map((modua) => (
              <tr key={modua} className="hover:bg-slate-50 transition-colors">
                <td className="px-6 py-4 font-semibold capitalize text-slate-600 bg-slate-50/50">{modua}</td>
                {DENBORAK.map((denbora) => {
                  const solution = aditzData?.aditzak[modua]?.[denbora];
                  const isInvalid = !solution;
                  const key = `${modua}-${denbora}`;
                  
                  return (
                    <td key={denbora} className="px-6 py-4">
                      {isInvalid ? (
                        <div className="h-10 bg-slate-100 rounded-md opacity-40 cursor-not-allowed" />
                      ) : (
                        <div className="space-y-2">
                          <input
                            type="text"
                            value={userAnswers[key] || ''}
                            onChange={(e) => handleInputChange(modua, denbora, e.target.value)}
                            disabled={showSolutions}
                            className={`w-full px-3 py-2 rounded border outline-none transition-all ${
                              results[key] === true ? 'border-green-500 bg-green-50' : 
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

      <footer className="mt-8 flex justify-center gap-4">
        <button 
          onClick={() => refetch()}
          disabled={isFetching}
          className="px-6 py-2 bg-slate-200 text-slate-700 rounded-full font-medium hover:bg-slate-300 transition-all disabled:opacity-50"
        >
          {isFetching ? 'Berrizten...' : 'Birsortu'}
        </button>
        <button 
          onClick={checkAnswers}
          className="px-6 py-2 bg-indigo-600 text-white rounded-full font-medium hover:bg-indigo-700 shadow-md hover:shadow-indigo-200 transition-all"
        >
          Zuzendu
        </button>
        <button 
          onClick={() => setShowSolutions(!showSolutions)}
          className="px-6 py-2 border-2 border-indigo-600 text-indigo-600 rounded-full font-medium hover:bg-indigo-50 transition-all"
        >
          {showSolutions ? 'Ozkutu' : 'Erantzuna ikusi'}
        </button>
      </footer>
    </div>
  );
};

export default Home;