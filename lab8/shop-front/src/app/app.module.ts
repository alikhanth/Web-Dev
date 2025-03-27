import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ProductListComponent } from './components/product-list/product-list.component';
import { ProductDetailComponent } from './components/product-detail/product-detail.component';
import { CategoryListComponent } from './components/category-list/category-list.component';
import { CategoryDetailComponent } from './components/category-detail/category-detail.component';
import { CategoryProductsComponent } from './components/category-products/category-products.component';
import { ApiService } from './services/api.service';

@NgModule({
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule,
    AppComponent,  // Import the components instead of declaring them
    ProductListComponent,
    ProductDetailComponent,
    CategoryListComponent,
    CategoryDetailComponent,
    CategoryProductsComponent
  ],
  providers: [ApiService],
})
export class AppModule { }
