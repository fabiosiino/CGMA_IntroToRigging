from maya import cmds
from maya import OpenMaya 
import sys

class BlendChains():
    
    def __init__(self):
        return
        
        
    def createBlend(self,  IkChain, FkChain, BindChain, SwitchCon):
        
        self.IkChain = IkChain
        self.FkChain = FkChain
        self.BindChain = BindChain
        self.SwitchCon = SwitchCon
        
        self.selection = [self.IkChain, self.FkChain, self.BindChain, self.SwitchCon]
        self.orientConList = []
        
        if len(self.selection) == 4:
            
            self.ctl = self.selection[3]
            
            
            if self.ctl.find("_CTL") != (-1):
                if cmds.attributeQuery("IKFK", n= self.ctl, exists=1) ==1:
                    cmds.deleteAttr(self.ctl + ".IKFK")
            cmds.addAttr(self.ctl, ln="IKFK", at="float", min=0, max=10, dv = 0)
            cmds.setAttr (self.ctl+ ".IKFK", e=1, keyable=1)
        
            
            #### Checking if joint chains are in correct order ####
            if "IK" in self.selection[0]:
                self.ikChain = [self.selection[0]]
                for each in cmds.listRelatives(self.selection[0], ad=1):
                    self.ikChain.append(each)
                self.ikChain.sort()
            else :
                OpenMaya.MGlobal.displayError(self.selection[0] + " is not a IK joint, you must select a valid FK joint")
                sys.exit()
            
            if "FK" in self.selection[1]:
                self.fkChain = [self.selection[1]]
                for each in cmds.listRelatives(self.selection[1], ad=1):
                    self.fkChain.append(each)
                self.fkChain.sort()
            else :
                OpenMaya.MGlobal.displayError(self.selection[1] + " is not an FK joint, you must select a valid IK joint")
                sys.exit()
                
            if "Bind" in self.selection[2]:
                self.bindChain = [self.selection[2]]
                for each in cmds.listRelatives(self.selection[2], ad=1):
                    self.bindChain.append(each)
                self.bindChain.sort()
            else :
                OpenMaya.MGlobal.displayError(self.selection[2] + " is not a Bind joint, you must select a valid Bind joint")
                sys.exit()
            
            ### Checking if the 3 chains have same length ###
            if len(self.bindChain) == len(self.fkChain) and len(self.bindChain) == len(self.ikChain) :
                #### Creating orient constraints ####
                for i in range(len(self.bindChain)):
                    self.orientCon = cmds.orientConstraint(self.ikChain[i], self.fkChain[i], self.bindChain[i], mo=1)
                    self.orientConList.append(self.orientCon[0])
                    cmds.setAttr(self.orientCon[0] + ".interpType", 2)
            else :
                OpenMaya.MGlobal.displayError( "The 3 selected chains have different lengths" )
            
            
            self.multiDNode = cmds.createNode("multiplyDivide", n=(self.bindChain[0].split("Bind_JNT")[0]+"Switch_MLT"))
            self.reverseNode = cmds.createNode("reverse", n=(self.bindChain[0].split("Bind_JNT")[0]+"Switch_RVS"))
            cmds.setAttr(self.multiDNode + ".input2X", 0.1)
            cmds.connectAttr(self.ctl + ".IKFK", self.multiDNode + ".input1X")
            cmds.connectAttr(self.multiDNode + ".outputX", self.reverseNode + ".inputX")
            
            for i in range (len(self.orientConList)):
                cmds.connectAttr(self.multiDNode + ".outputX", self.orientConList[i] + "." + self.fkChain[i] + "W1")
                cmds.connectAttr(self.reverseNode + ".outputX", self.orientConList[i] + "."  + self.ikChain[i] + "W0" )
            
        
            
        else:
            OpenMaya.MGlobal.displayError("Make sure to select in order IK - FK - Bind root joints and the switch controller")




class BlendingChainsUI():
   
    
    def addIkSel( *args):
        sel = cmds.ls(sl=True)
        add = cmds.textField('IKtFld', edit=True, text=sel[0])
    
    def addFkSel( *args):
        sel = cmds.ls(sl=True)
        add = cmds.textField('FKtFld', edit=True, text=sel[0])
    
    def addBindSel( *args):
        sel = cmds.ls(sl=True)
        add = cmds.textField('BindtFld', edit=True, text=sel[0])
    
    def addSwitchCon( *args):
        sel = cmds.ls(sl=True)
        add = cmds.textField('switchtFld', edit=True, text=sel[0])
    
    def blendChains(self, *args):
        textField_ikChain = cmds.textField( 'IKtFld', query=True, text=True )
        textField_fkChain = cmds.textField( 'FKtFld', query=True, text=True )
        textField_bindChain = cmds.textField( 'BindtFld', query=True, text=True )
        textField_switchCon = cmds.textField( 'switchtFld', query=True, text=True )
        
        BlendChains().createBlend(textField_ikChain, textField_fkChain, textField_bindChain, textField_switchCon)
       
    def blendChainsUI(self):
       
        # Define an id string for the window first
        self.wind = 'ITR - Blending Chains 1.0'
        
        # Test to make sure that the UI isn't already active
        if cmds.window(self.wind, exists=True) == 1 :
            cmds.deleteUI(self.wind)

        # Now create a fresh UI window
        self.win = cmds.window(self.wind)
        
        cmds.columnLayout(adjustableColumn=True)
        cmds.separator( height=50, style='out' )

        cmds.text(label = "Instructions : Insert FK - IK - Bind root joints, Insert switch control and run Blend Chains")
        cmds.separator( height=50, style='out' )
        
        cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 150), (2, 350)] )
        
       
        self.IKButton=cmds.button(l='IK Chain', c=self.addIkSel, width = 80, h=50)
        self.IKTextFld=cmds.textField('IKtFld',  h=50 , w=50 )
        
        
        
        self.FKButton=cmds.button(l='FK Chain', c=self.addFkSel, width = 80, h=50)
        self.FKTextFld=cmds.textField('FKtFld',  h=50, w=50)
        
      
        self.BindButton=cmds.button(l='Bind Chain', c=self.addBindSel, width = 80, h=50)
        self.BindTextFld=cmds.textField('BindtFld',  h=50, w=50)
        
      
        
        self.switchButton=cmds.button(l='Switch Con', c=self.addSwitchCon,  width = 80,  h=50) 
        self.switchTextFld=cmds.textField('switchtFld', h=50, w=50)
        
        cmds.setParent( '..' )
        
        cmds.separator( height=50, style='out' )
        self.switchButton=cmds.button(l='Blend Chains', c=self.blendChains, h=100,  width = 200)
        
        # Display the window
        cmds.showWindow(self.win)
                
                                
                                                                
BlendingChainsUI().blendChainsUI()   