from PIL import Image, ImageDraw

def dessiner_silhouette(couleur_hex, taille=120):
    hex_color = couleur_hex.lstrip('#')
    c = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    w = int(taille * 0.65)
    h = taille
    # Création d'une image transparente
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    s = taille / 120
    cx = w // 2

    # Tête
    r_tete = int(11 * s)
    cy_tete = int(12 * s)
    draw.ellipse([cx - r_tete, cy_tete - r_tete,
                  cx + r_tete, cy_tete + r_tete], fill=c)

    # Cou
    cou_w = int(5 * s)
    cou_y1 = cy_tete + r_tete
    cou_y2 = cou_y1 + int(4 * s)
    draw.rectangle([cx - cou_w, cou_y1, cx + cou_w, cou_y2], fill=c)

    # Épaules
    epaule_y1 = cou_y2
    epaule_y2 = epaule_y1 + int(6 * s)
    epaule_x1 = cx - int(16 * s)
    epaule_x2 = cx + int(16 * s)
    draw.rectangle([epaule_x1, epaule_y1, epaule_x2, epaule_y2], fill=c)

    # Corps + bassin
    tronc_x1 = cx - int(11 * s)
    tronc_x2 = cx + int(11 * s)
    tronc_y1 = epaule_y2
    tronc_y2 = tronc_y1 + int(35 * s)
    draw.rectangle([tronc_x1, tronc_y1, tronc_x2, tronc_y2], fill=c)

    # Bras gauche
    bras_w = int(5 * s)
    bras_h = int(22 * s)
    bras_y1 = epaule_y1 + int(2 * s)
    bras_y2 = bras_y1 + bras_h
    draw.rectangle([epaule_x1, bras_y1, epaule_x1 + bras_w, bras_y2], fill=c)

    # Bras droit
    draw.rectangle([epaule_x2 - bras_w, bras_y1, epaule_x2, bras_y2], fill=c)

    # Jambe gauche
    jambe_w = int(8 * s)
    jambe_h = int(28 * s)
    draw.rectangle([tronc_x1, tronc_y2,
                    tronc_x1 + jambe_w, tronc_y2 + jambe_h], fill=c)

    # Jambe droite
    draw.rectangle([tronc_x2 - jambe_w, tronc_y2,
                    tronc_x2, tronc_y2 + jambe_h], fill=c)

    return img

def generer_grille(nb_rouge, total=100, cols=10, rows=10, taille_sil=80, pad_x=12, pad_y=12):
    cell_w = int(taille_sil * 0.65)
    cell_h = taille_sil
    
    grid_w = cols * cell_w + (cols - 1) * pad_x
    grid_h = rows * cell_h + (rows - 1) * pad_y
    
    grid_img = Image.new("RGBA", (grid_w, grid_h), (0, 0, 0, 0))
    
    img_rouge = dessiner_silhouette("#E24B4A", taille_sil)
    img_noir = dessiner_silhouette("#2C2C2A", taille_sil)
    
    for i in range(total):
        col = i % cols
        row = i // cols
        
        x = col * (cell_w + pad_x)
        y = row * (cell_h + pad_y)
        
        sil = img_rouge if i < nb_rouge else img_noir
        grid_img.paste(sil, (x, y), sil)
        
    return grid_img

if __name__ == "__main__":
    # Génération pour 2016 : 86 rouges (rural), 14 noirs (urbain)
    grid_2016 = generer_grille(nb_rouge=86)
    grid_2016.save("picto_2016.png")
    print("picto_2016.png généré.")

    # Génération pour 2022 : 84 rouges (rural), 16 noirs (urbain)
    grid_2022 = generer_grille(nb_rouge=84)
    grid_2022.save("picto_2022.png")
    print("picto_2022.png généré.")
