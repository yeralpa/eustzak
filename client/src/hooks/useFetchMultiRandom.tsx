import { useQuery } from '@tanstack/react-query';
import axios from "axios";

export type RandomItem = {
    infinitiboa: string;
    modua: string;
    denbora: string;
    nor: string;
    nori: string;
    nork: string;
    aditza: string;
}

type MultiRandom = {
    success: boolean;
    items: RandomItem[];
}

export const useFetchMultiRandom = (n: number) => {
    return useQuery({
        queryKey: ["multiRandom", n],
        queryFn: () => axios.get<MultiRandom>(`${process.env.REACT_APP_API_URL}/conjugations/random?n=${n}`),
        staleTime: Infinity,
        refetchOnWindowFocus: false
    });
}
