import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = '/api/';

  constructor(private http: HttpClient) { }

  getProducts(): Observable<any> {
    return this.http.get(`${this.baseUrl}/products/`);
  }

  getProduct(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/products/${id}/`);
  }

  //getCategories(): Observable<any> {
  //  return this.http.get(`${this.baseUrl}/categories/`);
  //}

  getCategory(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/categories/${id}/`);
  } 
  getCategories() {
    return this.http.get<{ categories: { name: string }[] }>('/api/categories/');
  }
  

  getProductsByCategory(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/categories/${id}/products/`);
  } 

  deleteProduct(productId: number) {
    return this.http.delete(`/api/products/${productId}`);
  }
}  