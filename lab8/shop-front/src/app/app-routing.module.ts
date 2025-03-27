import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductListComponent } from './components/product-list/product-list.component';
import { ProductDetailComponent } from './components/product-detail/product-detail.component';
import { CategoryListComponent } from './components/category-list/category-list.component';
import { CategoryDetailComponent } from './components/category-detail/category-detail.component';
import { CategoryProductsComponent } from './components/category-products/category-products.component';

const routes: Routes = [
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent },
  { path: 'categories', component: CategoryListComponent },
  { path: 'categories/:id', component: CategoryDetailComponent },
  { path: 'categories/:id/products', component: CategoryProductsComponent },
  { path: '', redirectTo: '/products', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
