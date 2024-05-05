import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import {
  GetHistoryResponse,
} from "./types";

export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "http://127.0.0.1:5000",
 }),
  reducerPath: "main",
  tagTypes: ["history"],
  endpoints: (build) => ({
    getHistory: build.query<Array<GetHistoryResponse>, void>({

      query: () => "api/history",
      providesTags: ["history"],
    }),
  }),
});
console.log("value of api:",api);

export const { useGetHistoryQuery } =
  api;
