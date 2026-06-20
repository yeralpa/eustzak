import { routerType } from "../types/router.types";
import Home from "./Home";
import JolasaTaula from "./Jolasak/taula";

const pagesData: routerType[] = [
  {
    path: "",
    element: <Home />,
    title: "Eustzak"
  },
  {
    path: "/jolasa/taula",
    element: <JolasaTaula />,
    title: "E | Taula"
  }
];

export default pagesData;
