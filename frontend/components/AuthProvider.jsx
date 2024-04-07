import { useContext, createContext, useState, useEffect } from 'react';
import {SecureStore} from 'expo';

const AuthContext = createContext({
    token: null,
    setToken: () => {},
    isAuthenticated: false,
    getToken: () => {},
    logout: () => {},
});

export const useAuth = () => useContext(AuthContext);

export function AuthProvider({ children }) {
    const [token, setToken] = useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const getToken = () => {
        return token;
    }

    const logout = async () => {
        setToken(null);
        setIsAuthenticated(false);
        await SecureStore.setItemAsync('token', null);
    }

    const setTokenC = (token) => {
        setToken(token);
        SecureStore.setItemAsync('token', token);
        setIsAuthenticated(true)
    }

    useEffect(() => {
        const getToken = async () => {
            const token = await SecureStore.getItemAsync('token');
            if (token) {
                setToken(token);
                setIsAuthenticated(true);
            }
        }

        getToken();
    }, []);



    return (
        <AuthContext.Provider value={{ token, setToken: setTokenC, isAuthenticated, getToken, logout }}>
            {children}
        </AuthContext.Provider>
    )
}