import axios from 'axios'

const userApi = axios.create({
    baseURL: 'http://localhost:8000/api/users/',
    // baseURL: 'https://mediminder-e6ow.onrender.com/api/user/',
});

export const getAllUsers = () => userApi.get('/');

export const createUser = (user) => userApi.post('/', user);

export const obtenerUsuario = (usuario) => userApi.get(`/${usuario}/`);