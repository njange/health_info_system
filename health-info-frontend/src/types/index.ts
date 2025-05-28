export interface HealthInfo {
    id: number;
    name: string;
    age: number;
    condition: string;
    treatment: string;
}

export interface User {
    id: number;
    username: string;
    email: string;
}

export type ApiResponse<T> = {
    data: T;
    message: string;
    status: number;
};