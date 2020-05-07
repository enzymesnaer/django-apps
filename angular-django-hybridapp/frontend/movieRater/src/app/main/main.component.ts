import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { error } from '@angular/compiler/src/util';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  

  constructor(
    private apiService: ApiService
  ) { }

  movies:any = [];
  selectedMovie = null;

  ngOnInit(): void {
    this.apiService.getMovies().subscribe(
      data => {
       this.movies = data
      },
      error => console.log(error)
    );
  }

  selectMovie(movie) {
    this.selectedMovie = movie;
  }

}
