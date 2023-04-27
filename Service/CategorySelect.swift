//
//  CategorySelect.swift
//  Service
//
//  Created by E2620986 on 26/1/2566 BE.
//
import SwiftUI
import Foundation

struct CategorySelect: View {
    @State private var selection: String? = nil
    var body: some View {
        NavigationView{
        VStack{
        
            NavigationLink(destination: ContentView(), tag: "A", selection: $selection) {

 
            }
                
            NavigationLink(destination: CategoryRegister(), tag: "B", selection: $selection) {
           

            }
                
            Button("Helper") {
                selection = "A"
            }
            .frame(width: 300, height:80)
            .background(Color.blue)
            .foregroundColor(Color.yellow)

            Button("Needy") {
                selection = "B"
            }
            .frame(width: 300, height:80)
            .background(Color.yellow)
            .foregroundColor(Color.blue)
          }
        .navigationTitle("")
        }
    }
}
struct CategorySelect_Previews: PreviewProvider {
        static var previews: some View {
   
                    CategorySelect()
                
            }
    
 }

