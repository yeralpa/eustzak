import { useQuery } from '@tanstack/react-query';
import axios from "axios";

export type Mota = 'nor' | 'nor-nori' | 'nor-nork' | 'nor-nori-nork';

export type FullTableParams = {
    aditza: string;
    mota: Mota;
};

type FullTableResponse = {
    success: boolean;
    mota: Mota;
    aditza: string;
    data: Record<string, Record<string, unknown>>;
};

export const useFetchFullTable = (params: FullTableParams | null) => {
    return useQuery({
        queryKey: ["full-table", params],
        queryFn: () => axios.get<FullTableResponse>(`${process.env.REACT_APP_API_URL}/full-table`, { params: params! }),
        enabled: !!params,
        staleTime: Infinity,
        refetchOnWindowFocus: false
    });
};
