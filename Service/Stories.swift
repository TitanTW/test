//
//  Stories.swift
//  Service
//
//  Created by E2620986 on 2/2/2566 BE.
//

import Foundation
import SwiftUI
struct Stories: View {
    var body: some View {
            NavigationView {
                VStack {
                    Text("Stray pets")
                        .frame(width: 380, height:30, alignment: .leading)
                        .font(.system(size:20, weight:.bold, design:.monospaced))
                    Image("Image")
                                .resizable()
                                .scaledToFit()
                                .padding([.leading, .trailing],10)
                                .padding(.bottom,200)
                    
                }
                .navigationTitle("Success stories")
            }
        
        }
}


struct Stories_Previews: PreviewProvider {
        static var previews: some View {
                   Stories()
            
            }
}
