# texto="""Hamas y la "promocion de la democracia" Noam Chomsky

# Hamas gano combinando una fuerte resistencia contra la ocupacion militar con la creacion de organizaciones sociales de base y de servicio a los pobres, una plataforma y una practica que probablemente haria ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo politicamente justo. Sin embargo, es útil recordar que en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967. ..

# La posición de Washington hacia las elecciones en Palestina ha sido coherente. Las elecciones fueron postergadas hasta la muerte de Yasser Arafat, que fue recibida como una oportunidad para la realización de la "visión" de Bush sobre un eventual Estado palestino democrativo, que es una palido y vago reflejo del consenso internacional sobre una acuerdo de dos entidades estatales en la zona, que Estados Unidos viene bloqueando desde hace 30 años....

# El compromiso formal de Hamas de "destruir Israel" lo pone a la par con Estados Unidos e Israel, que prometieron por mucho tiempo que no habria ningun "Estado palestino adicional" (aparte de Jordania", hasta que ambas naciones aflojaron parcialmente su posicion, para aceptar un mini Estado constituido por los fragmentos que queden despues que Israel se apropie de todas las partes de Palestina que desea....

# Simplemente como conjetura, imagine el lector una inversion de las circunstancias: que Hamas permitiese a los israelies vivir en cantones desparramados e invariables, virtualmente separados unos de otros, y en alguna pequeña parte de Jerusalen, mientras los palestinos construyen enormes asentamientos y proyectos de infraestructura para apoderarse de las tierras y los recursos de Israel, Y que, ademas Hamas acepte llamar a esos fragmentos "un Estado". Si se hicieran propuestas para esta empobrecida "categoria de Estado", nosotros nos sentiriamos, con razon, horrorizados. Pero con ese tipo de propuestas, la posicion de Hamas seria esencialmente igual a la de Estados Unidos e Israel."""
# buscar=texto.find("Israel.")
# extraccion=texto[1720:2380]
# print(buscar)
# print(extraccion)


#--------------------------------------------------------------

texto="""La123 sociedad francesa estaba dividida en estamentos dependiendo de sus clases sociales, el poder mas alto lo tenía el rey, detrás estaban la nobleza y el clero y el nivel mas bajo de poder lo tenia el tercer estado que estaba constituido por la burguesía, los artesanos y los campesinos.

Los Estados Generales eran una asamblea, compuesta por tres ordenes separados: el clero, la nobleza y el grupo formado por burguesía y campesinado. Este último orden se conoce como el tercer estadeo, término que usaremos para referirnos a él en lo sucesivo. Dicha asamblea se había citado por ultima vez en 1614 y el dramatismo de la situación obligó al gobierno a convocarla nuevamente.

Luis XVI cedió a las presiones de la reina María Antonieta y del conde de Artois y dio instrucciones para que varios regimientos extranjeros leales se concentraran en París y Versailles. Al mismo tiempo, Necker fue nuevamente destituido. El pueblo de París respondió con la insurrección ante estos actos de provocación; los disturbios comenzaron el 12 de julio, y las multitudes asaltaron y tomaron La Bastilla -una prisión real que simbolizaba el despotismo de los Borbones- el 14 de julio.

El 5 de octubre de 1789, las mujeres parisinas partieron desde los barrios obreros hacia la residencia real de Versailles, este suceso dió comienzo a la revolución.

A123 fines de 1792 comenzó el proceso de Convención contra Luis XVI, quien fue juzgado y condenado a la guillotina por mayoría de votos. El 21 de enero de 1793, Luis subió al cadalso, inconmovible hasta el último momento en el sentimiento de su inocencia. La noticia de la muerte del rey produjo indignación en Inglaterra, la que despidió al embajador o representante francés. Francia contestó declarando la guerra a Inglaterra y a Holanda, su aliada."""

# buscar=texto.find("A123")
# buscar1=texto.find("aliada.")
# extr=texto[1336:1788]
# print(f"{buscar}kk{buscar1}")
# print(extr)

#----------------------

buscar=texto.find("La123")
buscar1=texto.find("campesinos")
extr=texto[0:288]
print(f"{buscar}kk{buscar1}")
print(extr)
