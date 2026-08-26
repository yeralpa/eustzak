import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

export type DenboraOption  = { value: string; label: string };
export type ModuaOption   = { value: string; label: string; denborak: DenboraOption[] };
export type AditzaOption  = { value: string; label: string; motak: string[] };
export type PertsonaOption = { value: string; nor: string; nori: string; nork: string };

export type MetaResponse = {
    aditzak:  AditzaOption[];
    moduak:   ModuaOption[];
    pertsonak: PertsonaOption[];
};

export const useFetchMeta = () => {
    return useQuery({
        queryKey: ['meta'],
        queryFn: () => axios.get<MetaResponse>(`${process.env.REACT_APP_API_URL}/meta`),
        staleTime: Infinity,
        refetchOnWindowFocus: false,
    });
};
