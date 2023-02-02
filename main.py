class Part:

    #contador de partes especificadas
    created_parts = 0

    def __init__(self, intro_st, centradores, puntos):
        """

        :param intro_st: string
            nombre de la estación en la que se introduce la pieza por primera vez a la línea
        :param centradores: listado de centradores
            listado con objetos de tipo centradores que son los que utiliza la pieza
        :param puntos: listado de puntos
            listado con objetos de tipo punto que son los que se utilizan en el QZ para realizar las mediciones
        """

        # almacena los centradores y los puntos de medición
        self.centradores = centradores
        self.puntos = puntos

        # el tipo de producto será una pieza
        self.tipo = "pieza"
        self.entrada = intro_st

