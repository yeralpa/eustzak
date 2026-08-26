import { useQuery } from '@tanstack/react-query';
import axios from "axios";

type AditzakStructure = {
    [modua: string]: {
        [denbora: string]: string | undefined;
    };
};

export type FullParams = {
    aditza: string;
    nor: string;
    nori: string;
    nork: string;
};

type FullResponse = {
    success: boolean;
    infinitiboa: string;
    nor: string;
    nori: string;
    nork: string;
    aditzak: AditzakStructure;
};

export const useFetchFull = (params: FullParams | null) => {
    return useQuery({
        queryKey: ["full", params],
        queryFn: () => axios.get<FullResponse>(`${process.env.REACT_APP_API_URL}/table`, { params: params! }),
        enabled: !!params,
        staleTime: Infinity,
        refetchOnWindowFocus: false
    });
};
