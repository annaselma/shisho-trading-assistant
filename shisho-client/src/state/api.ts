import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import {
  GetHistoryResponse,
} from "./types";

export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:5000" }),
  reducerPath: "main",
  tagTypes: ["history"],
  endpoints: (build) => ({
    getHistory: build.query<Array<GetHistoryResponse>, void>({

      query: () => "history",
      providesTags: ["history"],
    }),
  }),
});
console.log("value of api:",api);

export const { useGetHistoryQuery } =
  api;
