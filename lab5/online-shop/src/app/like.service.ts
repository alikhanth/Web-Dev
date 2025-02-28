import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LikeService {
  
  // Get likes for an item
  getLikes(itemId: number): number {
    return parseInt(localStorage.getItem(`likes_${itemId}`) || '0', 10);
  }

  // Save likes for an item
  saveLikes(itemId: number, likes: number): void {
    localStorage.setItem(`likes_${itemId}`, likes.toString());
  }

  // Increase likes when user clicks
  likeItem(itemId: number): number {
    let likes = this.getLikes(itemId);
    likes++;
    this.saveLikes(itemId, likes);
    return likes;
  }
}
