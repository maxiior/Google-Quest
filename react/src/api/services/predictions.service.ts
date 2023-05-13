import http from "api/http";
import { endpoints } from "routes";

export const makePrediction = async (data: any) => {
  return await http.post(endpoints.POST_MAKE_PREDICTION, data);
};

export const getPredictions = async () => {
  return await http.get(endpoints.GET_MAKE_PREDICTION);
};
