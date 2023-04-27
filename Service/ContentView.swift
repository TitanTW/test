//
//  ContentView.swift
//  Service
//
//  Created by E2620986 on 19/1/2566 BE.
//

import SwiftUI
import FirebaseAuth
import WebKit

class AppViewModel: ObservableObject {

    let auth = Auth.auth()
    @Published var signedIn = false
    var isSignedIn: Bool {
        return auth.currentUser != nil
    }
    func signIn(email: String, password: String) {
        auth.signIn(withEmail: email, password: password) { [weak self] result, error in
            guard result != nil, error == nil else{
                return
            }
            DispatchQueue.main.async {
                // Success
                self?.signedIn = true
            }
        }
    }
    func signUp(email: String, password: String) {
        auth.createUser(withEmail: email, password: password) { [weak self]result, error in guard result != nil, error == nil else{
            return
        }
            DispatchQueue.main.async {
            // Success
                self?.signedIn = true
            
            }
        }
    }
}

        
struct ContentView: View {
    
    @EnvironmentObject var viewModel: AppViewModel
    //@StateObject private var viewModel = ServiceViewModel()
    
    var body: some View {
        NavigationView {
            if viewModel.signedIn {
                Text("You are signed in")
            
            }
            else {
                SignInView()
            }
        }
        .onAppear{
            viewModel.signedIn = viewModel.isSignedIn
        }
        }
         
}






           

 
                

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
        }
        
    }
 }

                    

 struct SignInView: View {
     @State private var email: String = ""
     @State private var password: String = ""
     @State private var readyToNavigate : Bool = false
     
     @EnvironmentObject var viewModel: AppViewModel
     
     var body: some View {
         
         VStack{
             Text("Username:")
                 .frame(width: 270, height:20, alignment: .leading)
             TextField("Enter Email Here", text:$email)
                 .textFieldStyle(RoundedBorderTextFieldStyle())
                 .padding([.leading, .trailing],70)
                 .padding(.bottom,30)
             
             Text("Password:")
                 .frame(width: 270, height:20, alignment: .leading)
             TextField("Enter Password Here", text:$password)
                 .textFieldStyle(RoundedBorderTextFieldStyle())
                 .padding([.leading, .trailing],70)
             
             Button(action:{
                 guard !email.isEmpty, !password.isEmpty else {
                     return
                 }
                    
                 viewModel.signIn(email: email, password: password)
                    }, label:{
                        Text("Sign In")
                            .foregroundColor(Color.white)
                            .frame(width: 200, height: 50)
                            .cornerRadius(8)
                            .background(Color.blue)
                    })
             NavigationLink("Create Account", destination: SignUpView())
                 .padding()
         }
    }
}
                    
                    
struct SignUpView: View {
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var readyToNavigate : Bool = false
    
    @EnvironmentObject var viewModel: AppViewModel
    
    var body: some View {
        
        VStack{
            Text("Username:")
                .frame(width: 270, height:20, alignment: .leading)
            TextField("Enter Username Here", text:$email
            )
            .textFieldStyle(RoundedBorderTextFieldStyle())
            .padding([.leading, .trailing],70)
            .padding(.bottom,30)
            
            Text("Password:")
                .frame(width: 270, height:20, alignment: .leading)
            TextField("Enter Password Here", text:$password)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding([.leading, .trailing],70)
            
            Button(action:{
                guard !email.isEmpty, !password.isEmpty else {
                    return
                }
                
                viewModel.signUp(email: email, password: password)
            }, label:{
                Text("Create Account")
                    .foregroundColor(Color.white)
                    .frame(width: 200, height: 50)
                    .cornerRadius(8)
                    .background(Color.blue)
            })
            NavigationLink("Create Account", destination: SignUpView())
            
        }
        .padding()
        
        Spacer()
        
        .navigationTitle("Create Account")
    }
        


}
