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
            return axios.get<Random>('http://127.0.0.1:8000/bulkRandom')
        },
        staleTime: 1000
    })
}