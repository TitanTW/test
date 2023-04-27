//
//  CategoryWait.swift
//  Service
//
//  Created by E2620986 on 26/1/2566 BE.
//
import SwiftUI
import Foundation
struct CategoryWait: View {
    var body: some View {
        VStack{
            
            Text("Please wait for approval via email or phone call")
    
                .font(.system(size:30, weight:.semibold, design:.monospaced))
                .frame(width: 380, height:350)
    

    }
    
}
struct CategoryWait_Previews: PreviewProvider {
    static var previews: some View {
                    CategoryWait()
            }
    
 }
}

