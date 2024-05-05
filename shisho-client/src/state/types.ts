
export interface GetHistoryResponse {
  time: string;
  open: number;
  high: number;
  low: number;
  close:number;
}

export interface GetTransactionsResponse {
  id: string;
  _id: string;
  __v: number;
  buyer: string;
  amount: number;
  productIds: Array<string>;
  createdAt: string;
  updatedAt: string;
}
