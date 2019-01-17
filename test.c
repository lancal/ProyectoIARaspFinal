#include <pocketsphinx.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main(int argc, char *argv[])
{
    ps_decoder_t *ps;
    cmd_ln_t *config;
    FILE *fh;
    char const *hyp, *uttid;
    int16 buf[512];
    int rv;
    int32 score;

    FILE * fp;

    config = cmd_ln_init(NULL, ps_args(), TRUE,
		         "-hmm", MODELDIR "/home/pi/ProyectoIARaspFinal/sphinx/cmusphinx/model_parameters/voxforge_es_sphinx.cd_ptm_4000",
		         "-lm", MODELDIR "/home/pi/ProyectoIARaspFinal/sphinx/es.20k/es-20k.lm",
	    		 "-dict", MODELDIR "/home/pi/ProyectoIARaspFinal/sphinx/es/es.dict",
		         NULL);
    if (config == NULL) {
	fprintf(stderr, "Failed to create config object, see log for details\n");
	return -1;
    }

    ps = ps_init(config);
    if (ps == NULL) {
	fprintf(stderr, "Failed to create recognizer, see log for details\n");
	return -1;
    }


    fh = fopen("tmp.wav", "rb");

    if (fh == NULL) {
	fprintf(stderr, "Unable to open input file tmp.wav\n");
	return -1;
    }

    rv = ps_start_utt(ps);

    while (!feof(fh)) {
	size_t nsamp;
	nsamp = fread(buf, 2, 512, fh);
	rv = ps_process_raw(ps, buf, nsamp, FALSE, FALSE);
    }

    rv = ps_end_utt(ps);
    hyp = ps_get_hyp(ps, &score);
    //printf("Tu dijiste: %s\n", hyp);

    fp = fopen ("tempSTT/tempSTT.txt","w");

    fprintf(fp, hyp);


    fclose(fh);
    ps_free(ps);
    cmd_ln_free_r(config);

    return 0;
}
