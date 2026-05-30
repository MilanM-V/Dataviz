from PIL import Image,ImageDraw

def dessiner_silhouette_proportionnelle(p_rural,couleur_rural="#E24B4A",couleur_urbain="#2C2C2A",taille=400):
    w=int(taille*0.65)
    h=taille
    
    mask=Image.new("L",(w,h),0)
    draw_mask=ImageDraw.Draw(mask)
    
    s=taille/120
    cx=w//2
    
    r_tete=int(11*s)
    cy_tete=int(12*s)
    draw_mask.ellipse([cx-r_tete,cy_tete-r_tete,
                  cx+r_tete,cy_tete+r_tete],fill=255)

    cou_w=int(5*s)
    cou_y1=cy_tete+r_tete
    cou_y2=cou_y1+int(4*s)
    draw_mask.rectangle([cx-cou_w,cou_y1,cx+cou_w,cou_y2],fill=255)

    epaule_y1=cou_y2
    epaule_y2=epaule_y1+int(6*s)
    epaule_x1=cx-int(16*s)
    epaule_x2=cx+int(16*s)
    draw_mask.rectangle([epaule_x1,epaule_y1,epaule_x2,epaule_y2],fill=255)

    tronc_x1=cx-int(11*s)
    tronc_x2=cx+int(11*s)
    tronc_y1=epaule_y2
    tronc_y2=tronc_y1+int(35*s)
    draw_mask.rectangle([tronc_x1,tronc_y1,tronc_x2,tronc_y2],fill=255)

    bras_w=int(5*s)
    bras_h=int(22*s)
    bras_y1=epaule_y1+int(2*s)
    bras_y2=bras_y1+bras_h
    draw_mask.rectangle([epaule_x1,bras_y1,epaule_x1+bras_w,bras_y2],fill=255)

    draw_mask.rectangle([epaule_x2-bras_w,bras_y1,epaule_x2,bras_y2],fill=255)

    jambe_w=int(8*s)
    jambe_h=int(28*s)
    draw_mask.rectangle([tronc_x1,tronc_y2,
                    tronc_x1+jambe_w,tronc_y2+jambe_h],fill=255)

    draw_mask.rectangle([tronc_x2-jambe_w,tronc_y2,
                    tronc_x2,tronc_y2+jambe_h],fill=255)
    
    # Bottom p_rural% is couleur_rural,top (100-p_rural)% is couleur_urbain
    y_split=h-int(h*p_rural/100)
    
    color_img=Image.new("RGBA",(w,h),(0,0,0,0))
    draw_color=ImageDraw.Draw(color_img)
    
    hex_urbain=couleur_urbain.lstrip('#')
    c_urbain=tuple(int(hex_urbain[i:i+2],16) for i in (0,2,4))+(255,)
    draw_color.rectangle([0,0,w,y_split],fill=c_urbain)
    
    hex_rural=couleur_rural.lstrip('#')
    c_rural=tuple(int(hex_rural[i:i+2],16) for i in (0,2,4))+(255,)
    draw_color.rectangle([0,y_split,w,h],fill=c_rural)
    
    final_img=Image.new("RGBA",(w,h),(0,0,0,0))
    final_img.paste(color_img,(0,0),mask=mask)
    return final_img

if __name__ == "__main__":
    # Generate 2016 pictogram: 33% filled from bottom with red
    img_2016=dessiner_silhouette_proportionnelle(33,taille=400)
    img_2016.save("picto_2016.png")
    print("New picto_2016.png generated (33% filled).")
    
    # Generate 2022 pictogram: 34% filled from bottom with red
    img_2022=dessiner_silhouette_proportionnelle(34,taille=400)
    img_2022.save("picto_2022.png")
    print("New picto_2022.png generated (34% filled).")
