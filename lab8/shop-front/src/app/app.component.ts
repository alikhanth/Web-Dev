import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router'; 
import { ProductListComponent } from './components/product-list/product-list.component'; 

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,ProductListComponent], // ✅ Add to imports
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'shop-front';
}
