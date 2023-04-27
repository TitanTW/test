//
//  Database.swift
//  Service
//
//  Created by E2620986 on 26/3/2566 BE.
//

import Foundation
import FirebaseDatabase

final class ServiceViewModel: ObservableObject {
    @Published var ServiceDatabase: [Model] = []
    
    private lazy var databasePath: DatabaseReference? = {
        let ref = Database.database().reference().child("ServiceDatabase")
        return ref
    }()
    
    private let encoder = JSONEncoder()
    private let decoder = JSONDecoder()
    
    func listentoRealtimeDatabase() {
        guard let databasePath = databasePath else {
            return
        }
        databasePath
            .observe(.childAdded) { [weak self] snapshot in
                guard
                    let self = self,
                    var json = snapshot.value as? [String: Any]
                else {
                    return
                }
                json["id"] = snapshot.key
                do {
                    let accountData = try JSONSerialization.data(withJSONObject: json)
                    let account  = try self.decoder.decode(Model.self, from: accountData)
                    self.ServiceDatabase.append(account)
                } catch {
                    print("an error occurred", error)
                }
            }
    }
    
    func stopListening() {
        databasePath?.removeAllObservers()
    }
}
