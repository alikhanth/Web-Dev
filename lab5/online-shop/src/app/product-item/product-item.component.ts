import { Component, Input, Output, EventEmitter } from '@angular/core'; 
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-item',
  standalone: true, 
  imports:[CommonModule],
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css'],
})
export class ProductItemComponent { 
  
  @Input() product: any;
  @Input() index!: number;
  @Input() isLiked: boolean = false; 
  // Receive liked products set 
  @Input() currentProducts: any[] = [];
  @Output() remove = new EventEmitter<void>();
  @Output() like = new EventEmitter<number>();
  @Output() share = new EventEmitter<string>();
  @Output() likeChanged = new EventEmitter<void>(); // Emit an event
  onRemove() {
    this.remove.emit();
  }
  toggleLike() {
    this.like.emit();
  }
  
  onShare() {
    this.share.emit(this.product.link);
  }
}