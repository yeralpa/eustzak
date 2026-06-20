import { useQuery } from '@tanstack/react-query';
import axios from "axios";

type AditzakStructure = {
  [modua: string]: {
    [denbora: string]: string | undefined;
  };
};

type Random = {
    "success": boolean, 
    "infinitiboa": string,
    "nor": string,
    "nori": string,
    "nork": string,
    "aditzak": AditzakStructure
}

export const useFetchRandom = () => {
    return useQuery({
        queryKey: ["random"],
        queryFn: () => {
            return axios.get<Random>(`${process.env.REACT_APP_API_URL}/fullRandom`)
        },
        staleTime: Infinity, // Keep the data "fresh" so it doesn't auto-fetch
        refetchOnWindowFocus: false
    })
}