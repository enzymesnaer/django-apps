import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { faStar, faTrash, faEdit } from '@fortawesome/free-solid-svg-icons';
import { Movie } from 'src/app/models/Movie';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {

  faStar = faStar;
  faTrash = faTrash;
  faEdit = faEdit;
  

  @Input() movies: Movie[] = [];

  @Output() selectMovie = new EventEmitter<Movie>();

  @Output() editedMovie = new EventEmitter<Movie>();

  @Output() createNewMovie = new EventEmitter();

  @Output() deletedMovie = new EventEmitter<Movie>();

  

  constructor() {}
   
  ngOnInit() {}

  movieClicked(movie: Movie){
    this.selectMovie.emit(movie);
  }

  editMovie(movie: Movie){
    this.editedMovie.emit(movie);
  }

  newMovie(){
    this.createNewMovie.emit();
  }

  deleteMovie(movie: Movie){
    this.deletedMovie.emit(movie);
  }

}
