
import { UserButton } from '@clerk/nextjs';
import { SearchInput } from '@/components/search-input';
import prismaDb from '@/lib/prismadb';
import { Categories } from '@/components/categories';

const page = async () => {
	// const categories = await prismaDb.category.findMany();
	// const categories = await prismaDb.category.findMany();
	return (
		<div className='h-full p-4 space-y-2'>
			<SearchInput />
			{/* <Categories data={categories} /> */}
		</div>
	);
}


export default page