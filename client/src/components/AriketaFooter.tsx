type Props = {
    onBirsortu: () => void;
    onZuzendu: () => void;
    onToggleSolutions: () => void;
    isFetching: boolean;
    showSolutions: boolean;
};

const AriketaFooter = ({ onBirsortu, onZuzendu, onToggleSolutions, isFetching, showSolutions }: Props) => (
    <footer className="mt-8 flex justify-center gap-4">
        <button
            onClick={onBirsortu}
            disabled={isFetching}
            className="px-6 py-2 bg-slate-200 text-slate-700 rounded-full font-medium hover:bg-slate-300 transition-all disabled:opacity-50"
        >
            {isFetching ? 'Berrizten...' : 'Birsortu'}
        </button>
        <button
            onClick={onZuzendu}
            className="px-6 py-2 bg-indigo-600 text-white rounded-full font-medium hover:bg-indigo-700 shadow-md hover:shadow-indigo-200 transition-all"
        >
            Zuzendu
        </button>
        <button
            onClick={onToggleSolutions}
            className="px-6 py-2 border-2 border-indigo-600 text-indigo-600 rounded-full font-medium hover:bg-indigo-50 transition-all"
        >
            {showSolutions ? 'Ezkutu' : 'Erantzuna ikusi'}
        </button>
    </footer>
);

export default AriketaFooter;
