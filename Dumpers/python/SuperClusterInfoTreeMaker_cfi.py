import FWCore.ParameterSet.Config as cms

superclustertreemaker = cms.EDAnalyzer("SuperClusterTreeMaker",

    vertexCollection                  = cms.InputTag("offlinePrimaryVertices","","RECO"),
    caloParticleCollection            = cms.InputTag("mix","MergedCaloTruth","HLT"),
    ebSuperClusterCollection          = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALBarrel","RECO"), 
    eeSuperClusterCollection          = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALEndcapWithPreshower","RECO"), 
    
    doCompression                     = cms.bool(True),  #do the compression of floats
    nBits                             = cms.int32(12),   #nbits for float compression (<=23)
    doSimMatch                        = cms.bool(True),  #do matching with caloParticles

    genID                             = cms.vint32(22,11)  #save only caloParticles with this pdgId 
    #genID                            = cms.vdouble(0),  #save only caloParticles with this pdgId 
)