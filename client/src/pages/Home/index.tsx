import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const options = [
    {
        title: "Aditza Ariketa I",
        desc: "Aditza-taula bete.",
        path: "/jolasa/taula",
        accent: "border-emerald-500",
        text: "text-emerald-600"
    },
    {
      title: "Aditza Ariketa II",
      desc: "Klaseko ariketen antzekoa.",
      path: "/jolasa/errenkadak",
      accent: "border-indigo-500",
      text: "text-indigo-600"
    },
    {
      title: "Aditz Bilaketa",
      desc: "Hautatu pertsonak eta ikusi aditza forma guztiak.",
      path: "/jolasa/bilaketa",
      accent: "border-amber-500",
      text: "text-amber-600"
    },
    {
      title: "Aditz Bilaketa II",
      desc: "Hautatu mota eta ikusi taula osoak modu guztiekin.",
      path: "/jolasa/bilaketa2",
      accent: "border-violet-500",
      text: "text-violet-600"
    }
  ];

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6 font-sans">
      <div className="max-w-5xl w-full">

        <header className="text-center mb-16">
          <h1 className="text-5xl font-black text-slate-800 tracking-tight mb-3">
            Eus<span className="text-indigo-600">tzak</span>
          </h1>
          <p className="text-slate-500 text-lg">Euskal aditzak lantzeko tresna digitala</p>
        </header>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          {options.map((opt) => (
            <button
              key={opt.path}
              onClick={() => navigate(opt.path)}
              className={`group relative p-8 bg-white rounded-2xl border-b-4 ${opt.accent} shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all text-left`}
            >
              <h2 className={`text-2xl font-bold mb-2 ${opt.text}`}>
                {opt.title}
              </h2>
              <p className="text-slate-600 leading-relaxed">
                {opt.desc}
              </p>
              <div className="mt-6 flex items-center text-sm font-bold uppercase tracking-widest text-slate-400 group-hover:text-slate-800 transition-colors">
                Hasi proiektua 
                <span className="ml-2 group-hover:translate-x-1 transition-transform">→</span>
              </div>
            </button>
          ))}
        </div>

        <footer className="mt-20 border-t border-slate-200 pt-8 flex justify-between items-center text-slate-400 text-xs uppercase tracking-widest">
          <span>2026 • Eustzak</span>
          <div className="flex gap-4">
            <button className="hover:text-slate-800 transition-colors">Ezarpenak</button>
            <button className="hover:text-slate-800 transition-colors">Laguntza</button>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default Home;