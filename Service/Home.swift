//
//  Home.swift
//  Service
//
//  Created by E2620986 on 26/1/2566 BE.
//
import SwiftUI
//import Foundation

struct Home: View {
    @StateObject private var viewModel = ServiceViewModel()
    var body: some View {
        NavigationView {
            List(viewModel.ServiceDatabase) { account in
                HStack {
                    VStack {
                        Text(account.name).font(.headline)
                        /*  Text("Stray pets")
                         .font(.system(size:20, weight:.semibold, design:.monospaced))
                         
                         Image("Image")
                         .resizable()
                         .scaledToFit()
                         
                         Text("Special kids")
                         .font(.system(size:20, weight:.semibold, design:.monospaced))
                         Image("Image1")
                         .resizable()
                         .scaledToFit()*/
                        
                    }
                } .onAppear {
                    viewModel.listentoRealtimeDatabase()
                }
                .onDisappear {
                    viewModel.stopListening()
                }
                .navigationTitle("Home")
                
            }
        }
    }
    
    
    
    
    
    struct Home_Previews: PreviewProvider {
        
        static var previews: some View {
            Home()
            
        }
    }
}
