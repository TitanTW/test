//
//  CategorySelection.swift
//  Service
//
//  Created by E2620986 on 26/1/2566 BE.
//
import SwiftUI
import Foundation

struct CategoryRegister: View {
    @State private var orgName: String = ""
    @State private var orgInfo: String = ""
    @State private var orgNeeds: String = ""
    @State private var adminPhone: String = ""
    @State private var orgAddress: String = ""
    @State private var emailAddress: String = ""
    var body: some View {
        VStack {
            Group {
                Text("Organization's Name:")
           
                    .frame(width: 270, height:20, alignment: .leading)
                
                TextField("Enter Name Here", text:$orgName)
                
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding([.leading, .trailing],70)
                    .padding(.bottom,30)
                
            }
            
            Group{
                Text("Organization's Info:")
                    .frame(width: 270, height:20, alignment: .leading)
                TextField("Enter Info Here", text:$orgInfo)
                
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                  
                    .padding([.leading, .trailing],70)
                    .padding(.bottom,30)
            }
            
            Group{
            Text("Organization's needs:")
                    .frame(width: 270, height:20, alignment: .leading)
            TextField("Enter Here", text:$orgNeeds)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                      
                    .padding([.leading, .trailing],70)
                    .padding(.bottom,30)
                
            }
                    
            Group{
            Text("Admin's phone number:")
                .frame(width: 270, height:20, alignment: .leading)

            TextField("Enter Here", text:$adminPhone)
                
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                  
                    .padding([.leading, .trailing],70)
                    .padding(.bottom,30)
            }
            Group{
            Text("Organization's Address:")
                .frame(width: 270, height:20, alignment: .leading)

            TextField("Enter Here", text:$orgAddress)
                
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                  
                    .padding([.leading, .trailing],70)
                    .padding(.bottom,30)
            }
            Group{
            Text("Email Address:")
                .frame(width: 270, height:20, alignment: .leading)

            TextField("Enter Here", text:$emailAddress)
                
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                  
                    .padding([.leading, .trailing],70)
                    .padding(.bottom,30)
            }

        }
    }
}
struct CategoryRegister_Previews: PreviewProvider {
    static var previews: some View {
        CategoryRegister()
    }
}


