import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common'; 

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'], 
  imports: [CommonModule], // ✅ Import CommonModule for *ngFor
})
export class ProductListComponent implements OnInit {
    categories: string[] = [];
    products: any[] = [];
    filteredProducts: any[] = [];
    
    constructor(private apiService: ApiService) {}
  
    ngOnInit(): void {
      this.apiService.getCategories().subscribe(
        (data: any) => {
          console.log('Categories received:', data);
  
          if (Array.isArray(data)) {
            this.categories = data.map(category => category.name); // Extract category names
            this.products = data.flatMap((category: { name: string; products: any[] }) =>
              category.products.map((product: any) => ({ ...product, category: category.name }))
            ); 
            
  
            this.filteredProducts = [...this.products]; // Show all products initially
            console.log('Products:', this.products);
          } else {
            console.error("Unexpected API response format", data);
          }
        },
        error => {
          console.error("Error fetching categories:", error);
        }
      );
    }
  
    selectCategory(category: string): void {
      console.log('Selected category:', category);
  
      if (category === 'all') {
        this.filteredProducts = [...this.products];
      } else {
        this.filteredProducts = this.products.filter(product => product.category === category);
      }
  
      console.log('Filtered Products:', this.filteredProducts);
    }  

    removeProduct(productId: number): void {
      console.log(`Deleting product with ID: ${productId}`);
    
      this.apiService.deleteProduct(productId).subscribe(
        () => {
          console.log(`Product ${productId} deleted successfully!`);
    
          this.products = this.products.filter(product => product.id !== productId);
          this.filteredProducts = this.filteredProducts.filter(product => product.id !== productId);
    
          alert(`Product with ID ${productId} deleted successfully!`);
        },
        error => {
          console.error('Error deleting product:', error);
        }
      );
    }
    
    
  } 
  
  

  
  
