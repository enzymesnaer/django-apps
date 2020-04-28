import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { UploadService }  from '../upload.service';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  DJANGO_SERVER = 'http:///127.0.0.1:8000'
  form: FormGroup;
  response;
  fileURL;

  constructor(private formBuilder: FormBuilder, private uploadService: UploadService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      profile: ['']
    });
  }

  onChange(event){
    if(event.target.files.length > 0){
      const file = event.target.files[0];
      this.form.get('profile').setValue(file);
    }
  }

  onSubmit(){
    const formData = new FormData();
    formData.append('file', this.form.get('profile').value);

    this.uploadService.upload(formData).subscribe(

      (res)  => {
        this.response = res;
        this.fileURL = `${this.DJANGO_SERVER}${res.file}`;
        console.log(res);
        console.log(this.fileURL);
      },
      (err) => {
        console.log(err);
      }
     );
  }
}
