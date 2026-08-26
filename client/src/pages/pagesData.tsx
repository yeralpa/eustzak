import { routerType } from "../types/router.types";
import Home from "./Home";
import JolasaTaula from "./Jolasak/taula";
import Errenkadak from "./Jolasak/errenkadak";
import Bilaketa from "./Jolasak/bilaketa";
import Bilaketa2 from "./Jolasak/bilaketa2";

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
  },
  {
    path: "/jolasa/errenkadak",
    element: <Errenkadak />,
    title: "E | Ariketak"
  },
  {
    path: "/jolasa/bilaketa",
    element: <Bilaketa />,
    title: "E | Bilaketa"
  },
  {
    path: "/jolasa/bilaketa2",
    element: <Bilaketa2 />,
    title: "E | Bilaketa II"
  }
];

export default pagesData;
