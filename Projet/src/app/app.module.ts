import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app.routing';
import { ComponentsModule } from './components/components.module';
import { AppComponent } from './app.component';
import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { AboutUsComponent } from './about-us/about-us.component';
import {FlexmonsterPivotModule} from 'ng-flexmonster'; 
@NgModule({
  imports: [
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    ComponentsModule,
    RouterModule,
    AppRoutingModule,
    FlexmonsterPivotModule,
  
 
  ],
  declarations: [
    AppComponent,
    AdminLayoutComponent,
    AboutUsComponent,


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
