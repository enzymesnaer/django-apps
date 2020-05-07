import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(
    private httpClient: HttpClient
  ) { }

  baseUrl = 'http://localhost:8000/api/movies/';
  
  headers = new HttpHeaders({
    'Content-Type':'application/json',
    'Authorization': 'Token f513d33d6996009ce655384d9985e1e6e5cc6ba5'
  });

  private movies = ['Terminator', 'Predator'];


  getMovies(){
    return this.httpClient.get(this.baseUrl, {headers: this.headers});
  }

  rateMovies(rate: number, movieId){
    return this.httpClient.get(this.baseUrl, {headers: this.headers});
  }

}
