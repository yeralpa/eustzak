import { useMemo } from 'react';
import { MetaResponse, DenboraOption } from './useFetchMeta';

export const useAllDenborak = (meta: MetaResponse | undefined): DenboraOption[] =>
    useMemo(() => {
        if (!meta) return [];
        const seen = new Set<string>();
        const result: DenboraOption[] = [];
        for (const m of meta.moduak) {
            for (const d of m.denborak) {
                if (!seen.has(d.value)) { seen.add(d.value); result.push(d); }
            }
        }
        return result;
    }, [meta]);
