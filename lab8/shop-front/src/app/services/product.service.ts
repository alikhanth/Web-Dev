import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:8000/api/products/';

  constructor(private http: HttpClient) { }

  deleteProduct(productId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${productId}/`);
  }
}
