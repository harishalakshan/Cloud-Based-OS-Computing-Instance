import { createContext, useReducer } from 'react';

export const GlobalContext = createContext();

const initialState = { user: null, token: null };

function reducer(state, action) {
  switch(action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    default:
      return state;
  }
}
