import { useState } from 'react';

// Toggle a string in/out of a set. Prevents the set from becoming empty.
export const useToggleSet = (initial: Iterable<string> = []) => {
    const [set, setSet] = useState<Set<string>>(new Set(initial));
    const toggle = (value: string) => {
        setSet(prev => {
            const next = new Set(prev);
            if (next.has(value)) {
                if (next.size > 1) next.delete(value);
            } else {
                next.add(value);
            }
            return next;
        });
    };
    return [set, setSet, toggle] as const;
};
