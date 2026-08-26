import { AditzaOption } from '../hooks/useFetchMeta';

type Props = {
    aditzak: AditzaOption[];
    selected: Set<string>;
    onToggle: (value: string) => void;
};

const AditzakToggle = ({ aditzak, selected, onToggle }: Props) => (
    <div className="mb-4 flex flex-wrap justify-center gap-2">
        {aditzak.map(a => (
            <button
                key={a.value}
                type="button"
                onClick={() => onToggle(a.value)}
                className={`px-3 py-1.5 rounded text-sm font-medium border transition-colors ${
                    selected.has(a.value)
                        ? 'bg-indigo-600 text-white border-indigo-600'
                        : 'bg-white text-slate-500 border-slate-300 hover:border-indigo-400'
                }`}
            >
                {a.label}
            </button>
        ))}
    </div>
);

export default AditzakToggle;
