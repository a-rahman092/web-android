import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import emailjs, { EmailJSResponseStatus } from 'emailjs-com';
@Component({
  selector: 'parallax',
  templateUrl: './parallax.component.html',
  styleUrls: ['./parallax.component.css']
})
export class ParallaxComponent implements OnInit {
  constructor() { }

  ngOnInit(): void {
    
  }

  public sendEmail(e: Event) {
    e.preventDefault();
    emailjs.sendForm('service_3mi8ml8', 'template_vgotskl', e.target as HTMLFormElement, 'user_HelyhcwRRRSgJct2QVEOU')
      .then((result: EmailJSResponseStatus) => {
        console.log(result.text);
        alert("Form Successfully Submitted");
      }, (error) => {
        console.log(error.text);
      });
  }
  
}
  


